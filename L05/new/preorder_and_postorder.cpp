void preorder(TreeNode *root) {
    if(!root)
        return;
    cout<<root->val<<endl;
    preorder(root->left);
    preorder(root->right);
}


void postorder(TreeNode *root) {
    if(!root)
        return;
    preorder(root->left);
    preorder(root->right);
    cout<<root->val<<endl;
}