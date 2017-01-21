class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        if (root == nullptr) return result;
        stack<TreeNode*> nodes_ready_for_visiting;
        nodes_ready_for_visiting.emplace(root); // push new element on top of stack
        
        while (!nodes_ready_for_visiting.empty()) // iterate over nodes_ready_for_visiting
        {
            root = nodes_ready_for_visiting.top();
            nodes_ready_for_visiting.pop();
            result.emplace(result.end(), root->val); // ?
            
            if (root->right)
                nodes_ready_for_visiting.push(root->right);
            if (root->left)
                nodes_ready_for_visiting.push(root->left);
        }
        return result;
    }
};
