using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        var list = new List<int>();
        for (int i = 0; i < N; i++) {
            list.Add(int.Parse(Console.ReadLine()));
        }
        list.Sort();
        Console.WriteLine(string.Join("\n",list));
    }
}
