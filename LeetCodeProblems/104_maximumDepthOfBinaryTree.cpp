#include <cstddef>
#include <algorithm>
#include <queue>

/*
    Time Complexity: O(N) because we're going to visit every single node once
    Space Complexity: O(N)
*/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

//using DFS
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL){
            return 0;
        }

        return 1 + std::max(maxDepth(root->left), maxDepth(root->right));
    }
};


//using BFS
class Solution2 {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL){
            return 0;
        }

        int result = 0;
        std::queue<TreeNode*> q;
        q.push(root);
        

        while(!q.empty()){
            
            int qSize = q.size();
            for(int i = 0; i < qSize; i++){
                TreeNode* node = q.front();
                q.pop();

                if(node->left != NULL){
                    q.push(node->left);
                }

                if(node->right != NULL){
                    q.push(node->right);
                }
            }
            result ++;
        }
    }
};

