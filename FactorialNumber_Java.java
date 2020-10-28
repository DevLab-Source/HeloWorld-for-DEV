import java.util.Scanner;
public class FactorialNumber_Java {

    public static void main(String[] args) {

        int number;
        System.out.println("Enter the number: ");
        Scanner scanner = new Scanner(System.in);
        number = scanner.nextInt();
        scanner.close();
        long factorial = 1;
        for(int i = 1; i <= number; ++i)
        {
            factorial *= i;
        }
        System.out.println("Factorial of "+number+" is: "+factorial);
    }
}