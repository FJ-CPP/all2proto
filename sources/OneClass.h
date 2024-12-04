#include <string>

class OneClass {
public:
    OneClass();
    void method();

private:
    // basic types
    bool val_bool;
    char val_char;
    short val_short;
    int val_int;
    long val_long;
    long long val_long_long;
    float val_float;
    double val_double;

    // basic types with typedef
    int8_t val_int8_t;
    int16_t val_int16_t;
    int32_t val_int32_t;
    int64_t val_int64_t;
    uint8_t val_uint8_t;
    uint16_t val_uint16_t;
    uint32_t val_uint32_t;
    uint64_t val_uint64_t;

    // stl types
    std::string val_string;
    std::vector<int> val_vector;
    std::map<int, std::string> val_map;
    std::multimap<int, std::string> val_multimap;
    std::queue<int> val_queue;
    std::stack<int> val_stack;
    std::priority_queue<int> val_priority_queue;
    std::deque<int> val_deque;
    std::list<int> val_list;
    std::set<int> val_set;
    std::multiset<int> val_multiset;
    std::unordered_set<int> val_unordered_set;
    std::unordered_multiset<int> val_unordered_multiset;
    std::unordered_map<int, int> val_unordered_map;
    std::unordered_multimap<int, int> val_unordered_multimap;
};
