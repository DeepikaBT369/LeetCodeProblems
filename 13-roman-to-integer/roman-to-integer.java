import java.util.HashMap;
import java.util.Map;
//deepika
public class Solution{
    public static int romanToInt(String s){
        Map<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        int result = 0;

        for (int i=0; i<s.length(); i++){
            int value = romanMap.get(s.charAt(i));
            if(i<s.length()-1 && value<romanMap.get(s.charAt(i+1))){
                result-=value;
            }else{
                result +=value;
            }
        }
        return result; 
    }
    public static void main(String[] args){
        String roman = "MCMXCIV";
        System.out.println(romanToInt(roman));
    }
}
