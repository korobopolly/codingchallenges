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
        Console.WriteLine(N / 11 * 10);
    }
}
