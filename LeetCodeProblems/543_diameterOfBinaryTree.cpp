#include <cstddef>
#include <algorithm>

/*
    Time complexity: O(N)
    Space complexity: O(N)
*/

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    int ans = 0;

    int diameterOfBinaryTree(TreeNode* root) {
        dfs(root);
        return ans;
    }

private:
    int dfs(TreeNode* root){
        if(root == NULL){
            return 0;
        }

        int left = dfs(root->left);
        int right = dfs(root->right);
        ans = std::max(ans, left + right);
        return 1 + std::max(left, right);
    }
};