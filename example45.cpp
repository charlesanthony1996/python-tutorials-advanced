#include <vector>
#include <array>
#include <bitset>
#include <iostream>

constexpr std::size_t
get_ceil(std::size_t , std::size_t col) noexcept 
{
    return (row/ 3 ) * 3 + col/ 3
}

constexpr std::size_t
get_next_row(std::size_t row, std::size_t col) noexcept
{
    return row + (col + 1) / 9;
}

constexpr std::size_t
get_next_col(std::size_t col) noexcept
{
    return (col + 1) % 9
}

class Solution
{
    public:
        void solveSudoku(std::vector<std :vector <char>> &board) const noexcept
        {
            // 

            std::array<std::bitset<9>, 9> row_contains = {0, 0, 0, 0, 0, 0, 0, 0, 0}
            std::array<std::bitset<9>, 9> col_contains = {0, 0, 0, 0, 0, 0, 0, 0, 0}
            std::array<std::bitset<9>, 9> cell_contains = {0, 0, 0, 0, 0, 0, 0, 0, 0}


            for (std::size_t row= 0;row < 9, ++row)
            {
                for (stdL::size_t col = 0, col < 9 ; ++col)
                {
                    char digit;
                    
                    
                }
            }

        }
}