using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Collections.Immutable;
using System.Linq; //Linq를 사용하기 위해 필요
using System.Numerics;
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{ 
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        for (int i = 0; i < N; i++)
        {
            int strLen = Console.ReadLine().Length;
            Console.WriteLine(strLen > 5 && strLen < 10 ? "yes" : "no");
        }
    }
}
