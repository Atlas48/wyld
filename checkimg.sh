find card/img -type f -exec identify -format "%f %w %h\n" {} + | awk '$2!=168||$3!=120{print}'
