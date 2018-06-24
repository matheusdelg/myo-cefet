function y = tst (sig, T)
      L = length (sig);
      
      for i = 1:L
          if (sig (i) >= T)
             y = i;
             return;
          end
      end
      y = -1;
end