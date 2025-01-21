using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        while (true)
        {
            var input = Console.ReadLine()
                .Sum(x => x switch
                {
                    '1' => 3,
                    '0' => 5,
                    _ => 4
                }
            );
            if (input == 5) break;
            sb.AppendLine($"{input + 1}");
        }
        Console.WriteLine(sb.ToString());
    }
}
