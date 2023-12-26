class CreateComments < ActiveRecord::Migration[7.0]
  def change
    create_table :comments, id: false do |t|
      t.bigint :id, primary_key: true
      t.string :commentable_type, null: false
      t.integer :commentable_id, null: false
      t.string :owner_id
      t.text :body
      t.integer :score
      t.timestamps
      t.index [:commentable_type, :commentable_id], name: "index_comments_on_commentable"
    end
  end
end
