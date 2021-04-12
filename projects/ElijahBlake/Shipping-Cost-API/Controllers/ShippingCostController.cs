using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace ShippingCostAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class ShippingCostController : ControllerBase
    { 
        [HttpGet]
        public string Get(string ids)
        {
            WebRequest request = WebRequest.Create(
              "https://localhost:5001/Index/GetCosts/" + ids);
            WebResponse response = request.GetResponse();

            using (Stream dataStream = response.GetResponseStream())
            {
                StreamReader reader = new StreamReader(dataStream);
                string responseFromServer = reader.ReadToEnd();
                response.Close();
                return responseFromServer;
            }          
        }
    }
}
