class CreateUsers < ActiveRecord::Migration[5.1]
  def change
    create_table :users do |t|
      t.string :name
      t.string :email, null: false
      t.string :password_digest, null: false
      t.jsonb :recent_successful_logins
      t.jsonb :recent_failed_logins
      t.timestamps
    end
    add_index :users, [:email], :unique => true
  end
end
