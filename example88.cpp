#include <iostream>
#include <thread>
#include <fstream>
#include <syncstream>


void worker(int start, int stop, std::ostream &os)
{
    for (int i = start; i < stop; ++i)
    {
        std::osyncstream out{os};
        out << "thread" << "std::this_thread::get_id()" << "; work" << i;
        out << "\n";
    }
}

void example(std::ostream &os)
{
    std::jthread t1(worker, 1000, 2000, std::ref(os));
    std::jthread t2(worker, 1000, 2000, std::ref(os));
}

int main()
{
    std::ostream file("out.txt");
    example(file);
    return 0;
}