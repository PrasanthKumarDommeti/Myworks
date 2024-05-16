import java.util.*;
import java.lang.*;
import java.io.*;
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		
		while( t-- > 0 ){
		    String s = sc.next();
		    if( s.length() < 4 ){
		        System.out.println("Error");
		    }
            //It is the tags that can be start wth or end with the taged elements
		    else if( s.charAt(0) != '<' || s.charAt(s.length()-1) != '>' || s.charAt(1) != '/' ){
		        System.out.println("Error");
		    }
		    else{
		        boolean flag = true;
		        // Check wheather the element should be in the order of a-z or 0-9 between
		        for( int i = 2 ; i < s.length() - 1 ; i++  ){
		            if( ( s.charAt(i) >= 'a' && s.charAt(i) <= 'z' ) || (s.charAt(i) >= '0' && s.charAt(i) <= '9') ){
		                continue;
		            }
		            else{
		                flag = false;
		                break;
		            }
		        }
		        // If it can satisfies all the conditions then return true else false
		        if( flag ){
		            System.out.println("Success");
		        }
		        else{
		            System.out.println("Error");
		        }
		        
		    }
		    
		}
	}
}
