using System;
using System.Collections.Generic;
using System.Linq;
using System.Numerics;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;
using System.Security.Claims;
using System.Text;

class Program2
{
    static void Main(string[] args)
    {
        var input1 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int A1 = input1[0];
        int B1 = input1[1];
        var input2 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int A2 = input2[0];
        int B2 = input2[1];
        int LCM = (B1 / GCD(B1, B2)) * B2;

        int son = (A1 * (LCM / B1)) + (A2 * (LCM / B2));
        int mom = LCM;
        int divide = GCD(son, mom);
        Console.WriteLine(son / divide + " " + LCM / divide);
    }

    static int GCD(int A, int B)
    {
        if (B > A) { (A, B) = (B, A); }
        while (B != 0)
        {
            (A, B) = (B, A % B);
        }
        return A;
    }
}