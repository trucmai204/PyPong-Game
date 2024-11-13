let canvas = document.getElementById('pong');
let context = canvas.getContext('2d');
let screenWidth = canvas.width = 800;
let screenHeight = canvas.height = 600;

let ball = new Ball(screenWidth, screenHeight);
let leftPaddle = new Paddle(20, screenHeight / 2 - 50);
let rightPaddle = new Paddle(screenWidth - 30, screenHeight / 2 - 50);
let score = new Score(screenWidth);

function gameLoop() {
    context.clearRect(0, 0, screenWidth, screenHeight);

    ball.move();
    ball.bounce(screenHeight);

    leftPaddle.keepWithinBounds(screenHeight);
    rightPaddle.keepWithinBounds(screenHeight);

    ball.draw(context);
    leftPaddle.draw(context);
    rightPaddle.draw(context);
    score.update(context);

    let winner = score.checkWinner(5); // Ví dụ, chiến thắng khi đạt 5 điểm
    if (winner) {
        alert(winner);
        resetGame();
    }

    requestAnimationFrame(gameLoop);
}

function resetGame() {
    ball.reset(screenWidth, screenHeight);
    leftPaddle.y = screenHeight / 2 - 50;
    rightPaddle.y = screenHeight / 2 - 50;
    score.leftScore = 0;
    score.rightScore = 0;
}

gameLoop();  // Bắt đầu vòng lặp trò chơi
