using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0];
        int A = input[1];
        int B = input[2];

        int GoodOnion = 1;
        int BadOnion = 1;

        for (int i = 0; i < N; i++) {
            GoodOnion += A;
            BadOnion += B;

            if (GoodOnion < BadOnion)
            {
                (GoodOnion, BadOnion) = (BadOnion, GoodOnion);
            }
            else if (GoodOnion == BadOnion) {
                BadOnion -= 1;
            }
        }

        Console.WriteLine($"{GoodOnion} {BadOnion}");
    }
}