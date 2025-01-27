using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine();
        var list = new List<int>();
        for (int i = 0; i < input.Length; i++) {
            list.Add(input[i] - '0');
        }
        list.Sort();
        list.Reverse();
        Console.WriteLine(string.Join("",list));
    }
}
