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
        int M = input[1];
        var result = new List<int>();

        // 2차원 배열 선언
        string[,] board = new string[N, M];
        for (int i = 0; i < N; i++)
        {
            var line = Console.ReadLine();
            for (int j = 0; j < M; j++)
            {
                board[i, j] = line[j].ToString();
            }
        }

        // 8x8 체스판 탐색
        for (int startRow = 0; startRow <= N - 8; startRow++)
        {
            for (int startCol = 0; startCol <= M - 8; startCol++)
            {
                // 두 패턴에 대한 변경 횟수 계산
                int changesB = CalculateChanges(board, startRow, startCol, "B");
                int changesW = CalculateChanges(board, startRow, startCol, "W");
                result.Add(Math.Min(changesB, changesW)); // 최소 변경 횟수 저장
            }
        }

        Console.WriteLine(result.Min()); // 최소값 출력
    }

    // 체스판 변경 계산 함수
    static int CalculateChanges(string[,] board, int startRow, int startCol, string firstColor)
    {
        int count = 0;
        for (int i = 0; i < 8; i++)
        {
            for (int j = 0; j < 8; j++)
            {
                // 현재 칸에서 예상 색상
                string expectedColor = ((i + j) % 2 == 0) ? firstColor : (firstColor == "B" ? "W" : "B");

                // 실제 색상이 예상 색상과 다르면 변경 필요
                if (board[startRow + i, startCol + j] != expectedColor)
                {
                    count++;
                }
            }
        }
        return count;
    }
}
