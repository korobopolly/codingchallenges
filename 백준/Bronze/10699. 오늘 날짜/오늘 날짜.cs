using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        DateTime utc = DateTime.Now;
        DateTime seoul = utc.AddHours(9);
        Console.WriteLine(seoul.ToString("yyyy-MM-dd"));
    }
}