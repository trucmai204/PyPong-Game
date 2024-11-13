class Menu {
    constructor(screenWidth, screenHeight) {
        this.screenWidth = screenWidth;
        this.screenHeight = screenHeight;
        this.options = ["1 Player", "2 Players"];
        this.selectedOption = null;
    }

    draw(ctx) {
        ctx.fillStyle = "black";
        ctx.fillRect(0, 0, this.screenWidth, this.screenHeight);

        ctx.font = "74px Arial";
        ctx.fillStyle = "white";
        ctx.textAlign = "center";
        ctx.fillText("Select Mode", this.screenWidth / 2, 100);

        this.options.forEach((option, index) => {
            ctx.fillText(option, this.screenWidth / 2, 250 + index * 100);
        });
    }

    getSelectedOption(mouseX, mouseY) {
        for (let i = 0; i < this.options.length; i++) {
            let x = this.screenWidth / 2 - 100;
            let y = 250 + i * 100;
            if (mouseX >= x && mouseX <= x + 200 && mouseY >= y && mouseY <= y + 80) {
                this.selectedOption = this.options[i];
                return this.options[i];
            }
        }
        return null;
    }
}
