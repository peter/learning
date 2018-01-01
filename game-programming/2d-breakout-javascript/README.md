# 2D breakout game using pure JavaScript

## Canvas Basics

```javascript
// The Canvas context
var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");

// A red rectangle at x=20, y=40, width=50, height=60
ctx.beginPath();
ctx.rect(20, 40, 50, 60);
ctx.fillStyle = "#FF0000";
ctx.fill();
ctx.closePath();

// A green circle at x=240, y=160, radius=20, startAngle=0, endAngle=2*PI (radians), direction=clockwise
ctx.beginPath();
ctx.arc(240, 160, 20, 0, 1, false);
ctx.fillStyle = "green";
ctx.fill();
ctx.closePath();

// A rectangle with a border but no filling
ctx.beginPath();
ctx.rect(160, 10, 100, 40);
ctx.strokeStyle = "rgba(0, 0, 255, 0.5)";
ctx.stroke();
ctx.closePath();
```

## Making the Ball Move

```javascript
var x = canvas.width/2;
var y = canvas.height-30;
var dx = 2;
var dy = -2;

function drawBall() {
    ctx.beginPath();
    ctx.arc(x, y, 10, 0, Math.PI*2);
    ctx.fillStyle = "#0095DD";
    ctx.fill();
    ctx.closePath();
}

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawBall();
    x += dx;
    y += dy;
    if (x < 0) x = canvas.with
    if (x > canvas.width) x = 0
    if (y < 0) y = canvas.height
    if (y > canvas.height) y = 0
}

setInterval(draw, 10);
```

## Making the Ball Bounce

```JavaScript
var ballRadius = 10;

if(x + dx > canvas.width-ballRadius || x + dx < ballRadius) {
  dx = -dx;
}
if(y + dy > canvas.height-ballRadius || y + dy < ballRadius) {
    dy = -dy;
}
```

## Allowing the user to control the paddle

```javascript

```

## Resources

* [2D breakout game using pure JavaScript](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_Breakout_game_pure_JavaScript)
* [Radian (Wikipedia)](https://en.wikipedia.org/wiki/Radian)
