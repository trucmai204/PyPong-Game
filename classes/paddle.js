class Score {
    constructor(screenWidth, mode = 'single') {
        this.leftScore = 0;
        this.rightScore = 0;
        this.font = "48px Arial";  // Cài đặt phông chữ cho điểm số
        this.screenWidth = screenWidth;
        this.highScores = { single: 0, multi: 0 };  // Điểm cao mặc định
        this.mode = mode;
    }

    update(context) {
        context.font = this.font;
        context.fillStyle = "white";

        context.fillText(this.leftScore, this.screenWidth / 4, 50);
        context.fillText(this.rightScore, this.screenWidth * 3 / 4, 50);

        context.fillText("High Score: " + this.highScores[this.mode], this.screenWidth / 2 - 150, 100);
    }

    leftPoint() {
        this.leftScore++;
        this.updateHighScore();
    }

    rightPoint() {
        this.rightScore++;
        this.updateHighScore();
    }

    updateHighScore() {
        if (this.mode === 'single') {
            let currentHigh = this.highScores['single'];
            if (this.leftScore > currentHigh) {
                this.highScores['single'] = this.leftScore;
            } else if (this.rightScore > currentHigh) {
                this.highScores['single'] = this.rightScore;
            }
        } else {  // mode == 'multi'
            if (this.leftScore > this.highScores['multi']) {
                this.highScores['multi'] = this.leftScore;
            }
            if (this.rightScore > this.highScores['multi']) {
                this.highScores['multi'] = this.rightScore;
            }
        }
    }

    checkWinner(maxScore) {
        if (this.leftScore >= maxScore) return "Left Player Wins!";
        if (this.rightScore >= maxScore) return "Right Player Wins!";
        return null;
    }
}
