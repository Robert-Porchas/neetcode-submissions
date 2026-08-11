class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> sS;
        int end = 0;

        for(int i = 0; i < tokens.size();i++){
            if(tokens[i] == "/"){
                int x = sS.top();sS.pop();
                int y = (sS.top() / x); sS.pop();
                sS.push(y);
            } else if(tokens[i] == "*"){
                int x = sS.top();sS.pop();
                int y = (sS.top() * x); sS.pop();
                sS.push(y);
            } else if(tokens[i] == "+"){
                int x = sS.top();sS.pop();
                int y = (sS.top() + x); sS.pop();
                sS.push(y);
            } else if(tokens[i] == "-"){
                int x = sS.top();sS.pop();
                int y = (sS.top() - x); sS.pop();
                sS.push(y);
            } else {sS.push(stoi(tokens[i]));}
        }
        return sS.top();
    }
};
