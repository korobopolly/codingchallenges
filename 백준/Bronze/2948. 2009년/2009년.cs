using System;
using System.IO;
using System.Text;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int month = input[1];
        int day = input[0];
        
        DateTime specificDate = new DateTime(2009, month, day);
        DayOfWeek dayOfWeek = specificDate.DayOfWeek;
        Console.Write(dayOfWeek);
    }
}
