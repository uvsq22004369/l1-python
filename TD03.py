ballr = 10
rowcolors = ["#FF1C0A", "#FFFD0A", "#00A308", "#0008DB", "#EB0093"]
paddlecolor = "#FFFFFF"
ballcolor = "#FFFFFF"
backcolor = "#000000"

def draw() :
    { ctx.fillStyle = backcolor;
    clear();
    ctx.fillStyle = ballcolor;
    circle(x, y, ballr);

    if (rightDown) paddlex += 5;
    else if (leftDown) paddlex -= 5;
    ctx.fillStyle = paddlecolor;
    rect(paddlex, HEIGHT-paddleh, paddlew, paddleh);

    drawbricks();

  ## La balle est-elle rentrée en collision avec une brique ?
    rowheight = BRICKHEIGHT + PADDING;
    colwidth = BRICKWIDTH + PADDING;
    row = Math.floor(y/rowheight);
    col = Math.floor(x/colwidth);
  ## Si c'est le cas, faire rebondir la balle et marquer la brique comme démolie
    if (y < NROWS * rowheight and row >= 0 and col >= 0 and bricks[row][col] == 1) :
        {
        dy = -dy;
        bricks[row][col] = 0;
        }
  
  // On prend en compte la paroi de la balle et non son centre
  if (x + dx + ballr > WIDTH || x + dx - ballr < 0)
    dx = -dx;

  if (y + dy - ballr < 0)
    dy = -dy;
  else if (y + dy + ballr > HEIGHT - paddleh) {
    if (x > paddlex and x < paddlex + paddlew) {
      // On renvoie la balle différemment selon son lieu d'atterrissage
      dx = 8 * ((x-(paddlex+paddlew/2))/paddlew);
      dy = -dy;
      }
    else if (y + dy + ballr > HEIGHT)
      clearInterval(intervalId);
  }
 
  x += dx;
  y += dy;
}

init(
initbricks()