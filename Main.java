import java.util.Scanner;
public class Main {
    public static void main(String[]args){
        Scanner mt= new Scanner(System.in);
        int a=mt.nextInt();
        int b=mt.nextInt();
        int c=a+b;
        int d=a-b;
        int e=a*b;
        System.out.println("Addition: " + c);
        System.out.println("Subtraction: " + d);
        System.out.println("Multiplication: " + e);
    }
}
