class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> node_in_path;
        TreeNode* current_node = root;
        
        //left current right loop
        while (current_node || !node_in_path.empty())
        {
            while (current_node)
            {
                node_in_path.emplace(current_node);
                current_node = current_node->left; // loop left and push to node_in_path stack
            }
                
            current_node = node_in_path.top();// reach left leaf
            node_in_path.pop(); // pop left leaf
            result.push_back(current_node->val); // first get left key and then get current key and then right
            current_node = current_node->right;
        }
        
        return result;
    }
};
