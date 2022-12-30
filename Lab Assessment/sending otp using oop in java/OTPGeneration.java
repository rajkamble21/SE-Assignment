
import java.util.Random;

public class OTPGeneration {
    public static void main(String[] args) {
        String k = GOTP();
        System.out.println(k);
    }

    static String GOTP()
    {
        String UpCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String DownCase = "abcdefghijklmopqrstuvwxyz";
        //String SpeChar = "!@#$%^&*()_-+`~{}:?><:|";
        String Number = "0123456789";
        String Values = UpCase + DownCase + /*SpeChar +*/ Number;
        Random ran = new Random();
        StringBuilder BR = new StringBuilder();
        for(int i = 0; i < 8; i++)
        {
            BR.append(Values.charAt(ran.nextInt(Values.length())));
        }

        return BR.toString();
    }

    static String GG()
    {
        return "";
    }

}
