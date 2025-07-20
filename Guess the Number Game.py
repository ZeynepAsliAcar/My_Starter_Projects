import java.util.Random;
import java.util.Scanner;

class GuessingGame {
    private int randomNumber;
    private int attempts;
    private boolean isRunning;
    private Scanner input;

    public GuessingGame() {
        Random rand = new Random();
        this.randomNumber = rand.nextInt(100) + 1;
        this.attempts = 0;
        this.isRunning = true;
        this.input = new Scanner(System.in);
    }

    public void startGame() {
        System.out.println("Please guess a number between 1 and 100:");

        while (isRunning) {
            System.out.print("Enter your guess (or type 'quit' to exit): ");
            String userInput = input.nextLine();

            if (userInput.equalsIgnoreCase("quit")) {
                System.out.println("Oyundan çıkılıyor...");
                break;
            }

            int guess;
            try {
                guess = Integer.parseInt(userInput);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input! Please enter a valid number.");
                continue;
            }

            if (guess > 0 && guess <= 100) {
                attempts++;
                if (guess > randomNumber) {
                    System.out.println("You should enter a smaller value");
                } else if (guess < randomNumber) {
                    System.out.println("You should enter a bigger value");
                } else {
                    System.out.println("Your guess is correct, congratulations!");
                    System.out.println("You guessed it in " + attempts + " attempts.");
                    isRunning = false;
                }
            } else {
                System.out.println("Please enter a valid number between 1 and 100.");
            }
        }
    }
}

class GameRunner {
    public static void main(String[] args) {
        GuessingGame game = new GuessingGame();
        game.startGame();
    }
}