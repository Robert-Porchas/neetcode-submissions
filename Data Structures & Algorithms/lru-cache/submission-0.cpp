class LRUCache {
public:
    int size;
    std::unordered_map<int, int> keyLoc;
    std::list<int> cache;
    LRUCache(int capacity) {
        size = capacity;
    }
    
    int get(int key) {
        if(cache.remove(key) > 0){
            cache.push_front(key);
            return keyLoc[key];
        } else {
            return -1;
        }
    }
    
    void put(int key, int value) {
        if(cache.remove(key) > 0 ){
            cache.push_front(key);
            keyLoc[key] = value;
            return;
        } else {
            if(cache.size() >= size){
                cache.pop_back();
                cache.push_front(key);
                keyLoc[key] = value;
                return;
            }
            cache.push_front(key);
            keyLoc[key] = value;
            return;
        }
    }
};
