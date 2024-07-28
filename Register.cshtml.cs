using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;

namespace MyWebApp.Pages
{
    public class RegisterModel : PageModel
    {
        [BindProperty]
        public string Username { get; set; }

        [BindProperty]
        public string Password { get; set; }

        public void OnGet()
        {
        }

        public IActionResult OnPost()
        {
            if (ModelState.IsValid)
            {
                var user = new { Username, Password };
                var filePath = "users.json";
                List<object> users;

                // Read existing users from the file
                if (System.IO.File.Exists(filePath))
                {
                    var existingUsersJson = System.IO.File.ReadAllText(filePath);
                    users = JsonSerializer.Deserialize<List<object>>(existingUsersJson) ?? new List<object>();
                }
                else
                {
                    users = new List<object>();
                }

                // Add the new user to the list
                users.Add(user);

                // Serialize the list of users and write back to the file
                var options = new JsonSerializerOptions { WriteIndented = true };
                var json = JsonSerializer.Serialize(users, options);
                System.IO.File.WriteAllText(filePath, json);

                return RedirectToPage("Success");
            }
            return Page();
        }
    }
}
