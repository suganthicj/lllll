using System; 
  
public class GFG { 
      
    // Method to print the string 
    static public void printString(string str, 
                           char ch, int count) 
    { 
        int occ = 0, i; 
      
        // If given count is 0 
        // print the given string 
        // and return 
        if (count == 0) { 
            Console.WriteLine(str); 
            return; 
        } 
      
        // Start traversing the string 
        for (i = 0; i < str.Length; i++) 
        { 
      
            // Increment occ if current 
            // char is equal to given  
            // character 
            if (str[i] == ch) 
                occ++; 
      
            // Break the loop if given 
            // character has been occurred 
            // given no. of times 
            if (occ == count) 
                break; 
        } 
      
        // Print the string after the 
        // occurrence of given character 
        // given no. of times 
        if (i < str.Length - 1) 
            Console.WriteLine(str.Substring(i + 1)); 
      
        // Otherwise string is empty 
        else
            Console.WriteLine("Empty string"); 
    } 
      
    // Driver Method 
    static public void Main() 
    { 
        string str = "geeks for geeks"; 
        printString(str, 'e', 2); 
    } 
} 
  
