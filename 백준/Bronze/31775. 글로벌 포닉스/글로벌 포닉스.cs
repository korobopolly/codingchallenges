using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Text;

class Program2
{
    static void Main(string[] args)
    {
        int result = 0;
        for (int i = 0; i < 3; i++)
        {
            String input = Console.ReadLine();
            if (input[0] == 'l') {
                result += 2;
            }
            else if (input[0] == 'k')
            {
                result += 4;
            } 
            else if (input[0] == 'p') 
            { 
                result += 8; 
            }
        }
        Console.WriteLine(result == 14 ? "GLOBAL" : "PONIX");
    }
}