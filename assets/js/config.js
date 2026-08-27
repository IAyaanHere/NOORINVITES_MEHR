/**
 * CLIENT CONFIGURATION
 * --------------------
 * Change client-specific content here. Keep quotation marks and commas intact.
 * File paths are relative so this template works inside /khwahish/ or any folder.
 */

window.INVITATION_CONFIG = {
  site: {
    title: "Hiba & Zain — Baat Pakki Invitation",
    description:
      "You are warmly invited to celebrate the Baat Pakki of Hiba Fatima and Zain Ahmed.",
  },

  couple: {
    brideInitial: "Z",
    groomInitial: "Z",
    bride: {
      name: "Zoya Khan",
      shortName: "Zoya",
      relation: "Daughter of",
      parents: "Rashid Khan & Farida Begum",
    },
    groom: {
      name: "Shaikh Zaid",
      shortName: "Zaid",
      relation: "Son of",
      parents: "Shaikh Tariq & Shabana Begum",
    },
  },

  copy: {
    bismillah: "﷽",
    bismillahTranslation:
      "",
    welcomeLine: "With joyful hearts, we invite you\nto the Baat Pakki of",
    invitation:
      "",
    heroClosing: "",
    welcomeTitle: "Beautiful Beginning",
    welcomeBody:
      "With hearts full of joy, our families warmly invite you to celebrate this cherished evening of promises, blessings, and togetherness.",
    gifts:
      "Your love, blessings, and presence are the greatest gifts we could ever ask for.",
    closing: "We can’t wait to celebrate this special beginning with you.",
    dua: "بَارَكَ اللَّهُ لَكُمَا وَبَارَكَ عَلَيْكُمَا وَجَمَعَ بَيْنَكُمَا فِي خَيْرٍ",
    duaTranslation:
      "May Allah bless you both, shower His blessings upon you, and join you together in goodness.",
  },

  wedding: {
    // Use a valid ISO date with the local UTC offset for an accurate countdown.
    isoDate: "2026-10-18T19:00:00+05:30",
    date: "October 18, 2026",
    day: "Sunday",
    time: "07:00 PM",
    timezone: "IST",
  },

  media: {
    // Replace these two files inside the /media folder.
    introVideo: "./media/intro-placeholder.mp4",
    introPoster:
      "./media/intro-placeholder.webp",
    music: "./bismillah.mp3",

    // Replace gallery URLs with your own hosted files or image URLs.
    gallery: [
      {
        src: "./media/gallery/01.webp",
        alt: "A softly lit wedding detail",
        caption: "",
      },
      {
        src: "./media/gallery/02.webp",
        alt: "A joyful wedding celebration",
        caption: "",
      },
      {
        src: "./media/gallery/03.webp",
        alt: "Elegant wedding florals and table setting",
        caption: "",
      },
    ],
  },

  program: [
    {
      time: "6:30 PM",
      title: "Guest Arrival",
      note: "Welcome refreshments",
    },
    {
      time: "07:00 PM",
      title: "Baat Pakki Ceremony",
      note: "Promises shared with family blessings",
    },
    {
      time: "07:30 PM",
      title: "Family Blessings",
      note: "Greetings & photographs",
    },
    {
      time: "08:00 PM",
      title: "Dinner",
      note: "A feast shared with love",
    },
  ],

  venue: {
    name: "Noor Invites",
    address:
      "Mahal, Nagpur",
    mapUrl: "https://maps.app.goo.gl/9SjDC3RRg9jHZty59",
  },

dressCode: {
  title: "Festive Formal",
  description:
    "Traditional or formal attire is encouraged. Sarees, lehengas, anarkalis, sherwanis, kurtas, suits, and formal dresses are all welcome. We kindly ask guests to avoid overly casual attire and white or ivory.",
  swatches: [
    "#5D4C3E",
    "#8F917D",
    "#AE845E",
    "#8C6254",
    "#D8C7B5",
  ],
},

  preWeddingEvents: [],

  rsvp: {
    deadline: "Kindly respond by September 15, 2026",
    contact: "For assistance, call +91 98765 43210",
    fields: {
      name: "Your full name",
      email: "Email address",
      attendance: ["Joyfully accepts", "Regretfully declines"],
      guests: ["1 guest", "2 guests", "3 guests", "4 guests"],
      note: "Dietary notes or a message for the couple",
    },
  },

theme: {
  ivory: "#F3F0E9",       /* pearl bridal ivory */
  plum: "#5D4C3E",        /* deep warm cocoa */
  lavender: "#D8C7B5",    /* champagne blush */
  mauve: "#8C6254",       /* readable dusty rose */
  lilac: "#8F917D",       /* muted sage */
  champagne: "#AE845E",   /* antique gold */
},
};
