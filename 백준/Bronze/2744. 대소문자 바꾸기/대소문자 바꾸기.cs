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
        var input = Console.ReadLine();
        Console.WriteLine(InvertCase(input));
    }

    static string InvertCase(string input)
    {
        char[] chars = input.ToCharArray();
        for (int i = 0; i < chars.Length; i++) {
            if (char.IsLower(chars[i])) {
                chars[i] = char.ToUpper(chars[i]);
            }
            else
            {
                chars[i] = char.ToLower(chars[i]);
            }
        }
        return new string(chars);
    }
}
