using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Claims;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        string input = Console.ReadLine();
        for (char i = 'a'; i <= 'z'; i++) { 
            int count = input.Count(c => c == i);
            Console.Write(count + " ");
        }
    }
}