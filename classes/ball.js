class Ball {
    constructor(screenWidth, screenHeight) {
        this.x = screenWidth / 2;
        this.y = screenHeight / 2;
        this.radius = 10;
        this.dx = (Math.random() < 0.5 ? -1 : 1) * (Math.random() * (6 - 3) + 3);
        this.dy = (Math.random() < 0.5 ? -1 : 1) * (Math.random() * (6 - 3) + 3);
        this.color = "red";
        this.maxSpeed = 10;
    }

    move() {
        this.x += this.dx;
        this.y += this.dy;
    }

    draw(context) {
        context.beginPath();
        context.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        context.fillStyle = this.color;
        context.fill();
        context.closePath();
    }

    bounce(screenHeight) {
        if (this.y - this.radius < 0 || this.y + this.radius > screenHeight) {
            this.dy *= -1;
            // Tăng tốc độ bóng mỗi lần chạm vào cạnh trên hoặc dưới
            this.dx = Math.min(this.maxSpeed, this.dx * 1.05);
            this.dy = Math.min(this.maxSpeed, this.dy * 1.05);
        }
    }

    reset(screenWidth, screenHeight) {
        this.x = screenWidth / 2;
        this.y = screenHeight / 2;
        this.dx = -this.dx;
        this.dy = (Math.random() < 0.5 ? -1 : 1) * (Math.random() * (6 - 3) + 3);
    }
}
