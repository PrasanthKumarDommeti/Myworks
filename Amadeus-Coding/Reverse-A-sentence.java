import java.util.*;

public class Solution 
{
	public static String reverseString(String str) 
	{
		//Write your code here
		String[] arr = str.split(" ");
		Collections.reverse(Arrays.asList(arr));
		return String.join(" ", arr);
	}
}
