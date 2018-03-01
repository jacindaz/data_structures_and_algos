#!/usr/bin/env ruby
# by Andronik Ordian

def calc_fib(n)
  return n if n <= 1
  # slow
  # fix me
  calc_fib(n - 1) + calc_fib(n - 2)
end

if __FILE__ == $0
  n = gets.to_i
  puts "#{calc_fib(n)}"
end

def fibonacci(n)
  results = []
  results[0] = 0
  results[1] = 1

  index = 2
  (index..n).to_a.each do |number|
    add_prev_numbers = results[index - 1] + results[index - 2]

    puts "\n==================="
    puts "number: #{number}"
    puts "results[index-1]: #{results[index-1]}, results[index-2]: #{results[index-2]}"
    puts "add_prev_numbers: #{add_prev_numbers}"
    puts "===================\n"

    index += 1
    results << add_prev_numbers
  end

  puts "results: #{results}"
  results
end

fibonacci(10)
