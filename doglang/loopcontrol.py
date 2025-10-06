"""
Loop Control Module for DogLang

This module implements break and continue functionality for loops.
- 'heel' keyword acts as break (exits the loop immediately)
- 'stay' keyword acts as continue (skips to next iteration)

The module provides:
1. LoopControlError - Custom exception for invalid loop control usage
2. LoopControlHandler - Context manager for tracking loop control flow
3. Helper functions for validating and executing loop control statements
"""

from doglang.error import DogLangError

class LoopControlError(DogLangError):
    """Custom exception for loop control related errors"""
    def __init__(self, error_type, message):
        super().__init__(error_type, message)

class LoopControlHandler:
    """
    Context manager to handle break and continue statements within loops.
    Tracks the current loop context and handles control flow.
    """
    
    def __init__(self):
        self.should_break = False
        self.should_continue = False
        self.in_loop = False
    
    def __enter__(self):
        self.in_loop = True
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.in_loop = False
        # Reset flags after exiting loop context
        self.should_break = False
        self.should_continue = False
    
    def break_loop(self):
        """Signal that the current loop should be broken"""
        if not self.in_loop:
            raise LoopControlError("Syntax", "heel statement must be inside a loop")
        self.should_break = True
    
    def continue_loop(self):
        """Signal that the current loop should continue to next iteration"""
        if not self.in_loop:
            raise LoopControlError("Syntax", "stay statement must be inside a loop")
        self.should_continue = True
    
    def should_exit_loop(self):
        """Check if loop should be exited (break)"""
        return self.should_break
    
    def should_skip_iteration(self):
        """Check if current iteration should be skipped (continue)"""
        return self.should_continue
    
    def reset_flags(self):
        """Reset break and continue flags for next iteration"""
        self.should_break = False
        self.should_continue = False

# Global loop control handler instance
loop_control_handler = LoopControlHandler()

def execute_heel_statement():
    """
    Execute a 'heel' (break) statement.
    Raises LoopControlError if not used within a loop.
    """
    loop_control_handler.break_loop()

def execute_stay_statement():
    """
    Execute a 'stay' (continue) statement.
    Raises LoopControlError if not used within a loop.
    """
    loop_control_handler.continue_loop()

def should_break_loop():
    """Check if the current loop should be broken"""
    return loop_control_handler.should_exit_loop()

def should_continue_loop():
    """Check if the current iteration should be skipped"""
    return loop_control_handler.should_skip_iteration()

def reset_loop_control():
    """Reset loop control flags for next iteration"""
    loop_control_handler.reset_flags()

def enter_loop_context():
    """Enter a new loop context"""
    loop_control_handler.__enter__()

def exit_loop_context():
    """Exit the current loop context"""
    loop_control_handler.__exit__(None, None, None)

def validate_loop_control_context():
    """
    Validate that loop control statements are used in proper context.
    This should be called during semantic analysis.
    """
    # This will be used by the semantic analyzer to ensure
    # heel and stay are only used within loops
    pass

