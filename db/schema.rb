# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema[7.0].define(version: 2023_12_26_083441) do
  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "answers", primary_key: "answer_id", force: :cascade do |t|
    t.string "owner_id"
    t.bigint "question_id", null: false
    t.text "body"
    t.boolean "is_accepted"
    t.integer "comment_count"
    t.integer "score"
    t.string "link"
    t.integer "last_activity_date"
    t.integer "creation_date"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "comments", force: :cascade do |t|
    t.string "commentable_type", null: false
    t.integer "commentable_id", null: false
    t.string "owner_id"
    t.text "body"
    t.integer "score"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["commentable_type", "commentable_id"], name: "index_comments_on_commentable"
  end

  create_table "questions", primary_key: "question_id", force: :cascade do |t|
    t.string "title"
    t.string "owner_id"
    t.text "body"
    t.boolean "is_answered"
    t.integer "answer_count"
    t.integer "comment_count"
    t.integer "view_count"
    t.integer "score"
    t.string "link"
    t.integer "last_activity_date"
    t.integer "creation_date"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  add_foreign_key "answers", "questions", primary_key: "question_id"
end
