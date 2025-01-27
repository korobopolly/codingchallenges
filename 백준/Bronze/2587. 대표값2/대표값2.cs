using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        var list = new List<int>();
        for (int i = 0; i < 5; i++) { 
            list.Add(int.Parse(Console.ReadLine()));
        }
        list.Sort();
        Console.WriteLine(list.Sum()/5);
        Console.WriteLine(list[2]);
    }
}
