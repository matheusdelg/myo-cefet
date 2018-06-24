function y = ton (sig, T)
      L = length (sig);
      S = 15;
      r = [];
      
      for i = 1:(L-S)
          win = sig (i:i+S);
          if (rms (win) >= T)
              r = [r 1.0];
          else
              r = [r 0.0];
          end
      y = sum (r) / length (r);
end
