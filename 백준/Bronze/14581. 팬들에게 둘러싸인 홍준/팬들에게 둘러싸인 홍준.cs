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
        var input = Console.ReadLine();

        string fan = ":fan:";
        for (int i = 0; i < 3; i++) { 
            Console.Write(fan);
        }
        Console.WriteLine();
        Console.Write(fan);
        Console.Write(":" + input + ":");
        Console.Write(fan);
        Console.WriteLine();
        for (int i = 0; i < 3; i++)
        {
            Console.Write(fan);
        }
    }
}