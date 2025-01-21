using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine()
            .Select(x =>
                x switch
                {
                    >= 'A' and <= 'C' => 3,
                    >= 'D' and <= 'F' => 4,
                    >= 'G' and <= 'I' => 5,
                    >= 'J' and <= 'L' => 6,
                    >= 'M' and <= 'O' => 7,
                    >= 'P' and <= 'S' => 8,
                    >= 'T' and <= 'V' => 9,
                    >= 'W' and <= 'Z' => 10,
                    _ => 0                 
                });
        Console.WriteLine(input.Sum());
    }
}
