#!/usr/bin/env node
var fontkit = require('fontkit');
var argv = require('minimist')(process.argv.slice(2));

var font = fontkit.openSync(argv.font);

if (argv.variation) {
  let settings = {};
  argv.variation.split(';').forEach(function (setting) {
    var parts = setting.split(':');
    settings[parts[0]] = parts[1];
  });
  
  font = font.getVariation(settings);
}

var run = font.layout(argv.render);
var x = 0, y = 0;
var svg = run.glyphs.map(function (glyph, index) {
  var pos = run.positions[index];
  x += pos.xOffset;
  y += pos.yOffset;
  var path = transformPath(glyph.path, x, y);
  x += pos.xAdvance;
  y += pos.yAdvance;
  return path.toSVG().replace(/([A-Z])/g, '$1 ').replace(/(\d+) (-?\d+)/g, '$1,$2').replace(/(\d)([A-Z])/g, '$1 $2');
});

function transformPath(path, x, y) {
  var p = new path.constructor();
  p.commands = path.commands.map(function (c) {
    var res = {command: c.command, args: []};
    for (var i = 0; i < c.args.length; i += 2) {
      res.args.push(c.args[i] + x | 0);
      res.args.push(c.args[i + 1] + y | 0);
    }
    return res;
  });
  
  return p;
}

var descent = font.descent; // TODO
if (/TestKERNOne/.test(argv.font))
  descent--;

console.log('<?xml version="1.0" encoding="UTF-8"?>');
console.log('<svg viewBox="' + [0, descent, run.advanceWidth, font.ascent - descent].join(' ') + '"><g><path d="' + svg.join('\n') + '"></path></g></svg>');
