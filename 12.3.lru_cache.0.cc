#include <list>
#include <unordered_map>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/serialization_traits.h"
#include "test_framework/test_failure.h"

class LruCache {
    struct LruNode {
        LruNode(int isbn, int price) : isbn_(isbn), price_(price) {}
        int isbn_;
        int price_;
    };

    size_t capacity_;
    std::list<LruNode> lru_queue_;
    std::unordered_map<int,std::list<LruNode>::iterator> isbn_lookup_;
    void insert_node(int isbn, int price)
    {
        LruNode temp = {isbn, price};
        lru_queue_.push_front(temp);
        isbn_lookup_[isbn] = lru_queue_.begin();
        return;
    }
    void update_node(int isbn)
    {
        LruNode temp = {isbn_lookup_[isbn]->isbn_, isbn_lookup_[isbn]->price_};
        lru_queue_.erase(isbn_lookup_[isbn]);
        lru_queue_.push_front(temp);
        isbn_lookup_[isbn] = lru_queue_.begin();
        return;
    }
    void erase_node(int isbn)
    {
        lru_queue_.erase(isbn_lookup_[isbn]);
        isbn_lookup_.erase(isbn);
        return;
    }
    void erase_lru()
    {
        int isbn = lru_queue_.back().isbn_;
        isbn_lookup_.erase(isbn);
        lru_queue_.pop_back();
        return;
    }

public:
    LruCache(size_t capacity) :capacity_(capacity) {}
    int Lookup(int isbn)
    {
        // TODO - you fill in here.
        if (isbn_lookup_.find(isbn) == isbn_lookup_.end()) return -1;
        int price = isbn_lookup_[isbn]->price_;
        erase_node(isbn);
        insert_node(isbn, price);
        return lru_queue_.front().price_;
    }
    void Insert(int isbn, int price)
    {
        // TODO - you fill in here.
        if (Lookup(isbn) == -1) {
            insert_node(isbn, price);
        }
        else{
            update_node(isbn);
        }
        if (lru_queue_.size() > capacity_) {
            erase_lru();
        }
        return;
    }
    bool Erase(int isbn)
    {
        // TODO - you fill in here.
        if (Lookup(isbn) == -1) return false;
        erase_node(isbn);
        return true;
    }
};
struct Op {
    std::string code;
    int arg1;
    int arg2;
};

template <>
struct SerializationTraits<Op> : UserSerTraits<Op, std::string, int, int> {};

void RunTest(const std::vector<Op>& commands) {
    if (commands.empty() || commands[0].code != "LruCache") {
        throw std::runtime_error("Expected LruCache as first command");
    }
    LruCache cache(commands[0].arg1);

    for (int i = 1; i < commands.size(); i++) {
        auto& cmd = commands[i];
        if (cmd.code == "lookup") {
            int result = cache.Lookup(cmd.arg1);
            if (result != cmd.arg2) {
                throw TestFailure("Lookup: expected " + std::to_string(cmd.arg2) +
                        ", got " + std::to_string(result));
            }
        } else if (cmd.code == "insert") {
            cache.Insert(cmd.arg1, cmd.arg2);
        } else if (cmd.code == "erase") {
            bool result = cache.Erase(cmd.arg1);
            if (result != cmd.arg2) {
                throw TestFailure("Erase: expected " + std::to_string(cmd.arg2) +
                        ", got " + std::to_string(result));
            }
        } else {
            throw std::runtime_error("Unexpected command " + cmd.code);
        }
    }
}

int main(int argc, char* argv[]) {
    std::vector<std::string> args{argv + 1, argv + argc};
    std::vector<std::string> param_names{"commands"};
    return GenericTestMain(args, "lru_cache.cc", "lru_cache.tsv", &RunTest,
            DefaultComparator{}, param_names);
}
